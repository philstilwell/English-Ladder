// Custom passwords are salted and stretched, then protected by a separate
// Worker secret. Neither plaintext nor a reusable password digest is returned
// to the administrator browser. 100,000 is Workers' Web Crypto iteration cap.
const encoder = new TextEncoder();
const SCHEME = 'pbkdf2-sha256-hmac-v1';
const encode = bytes => btoa(String.fromCharCode(...new Uint8Array(bytes)));
const decode = value => Uint8Array.from(atob(value), c => c.charCodeAt(0));
const normalized = value => value.toLowerCase();
async function pepperKey(secret) {
  if (typeof secret !== 'string' || secret.length < 32) throw new Error('Student password settings are not ready. Please try again later.');
  return crypto.subtle.importKey('raw', encoder.encode(secret), { name:'HMAC', hash:'SHA-256' }, false, ['sign','verify']);
}
async function material(password, salt, accountKey) {
  const key = await crypto.subtle.importKey('raw', encoder.encode(normalized(password)), 'PBKDF2', false, ['deriveBits']);
  const bits = await crypto.subtle.deriveBits({ name:'PBKDF2', hash:'SHA-256', iterations:100000, salt:decode(salt) }, key, 256);
  return encoder.encode(JSON.stringify([SCHEME, accountKey, salt, encode(bits)]));
}
export async function makeStudentPassword(env, input, accountKey) {
  const password = input.newPassword;
  if (password == null || password === '') {
    if (input.confirmPassword) throw new Error('Enter the new password in both boxes.');
    return null;
  }
  if (typeof password !== 'string' || password.length < 6 || password.length > 128 || !password.trim() || /[\u0000-\u001f\u007f]/.test(password)) throw new Error('Use a student password with 6 to 128 characters.');
  if (typeof input.confirmPassword !== 'string' || normalized(password) !== normalized(input.confirmPassword)) throw new Error('The two student passwords do not match.');
  if (normalized(password) === normalized(env.TEACHER_PASSWORD || '')) throw new Error('Choose a student password different from your administrator password.');
  const key = await pepperKey(env.STUDENT_PASSWORD_PEPPER);
  const salt = encode(crypto.getRandomValues(new Uint8Array(16)));
  return { scheme:SCHEME, salt, hash:encode(await crypto.subtle.sign('HMAC', key, await material(password, salt, accountKey))) };
}
export async function matchesStudentPassword(env, credential, accountKey, password) {
  if (!credential || credential.scheme !== SCHEME) return false;
  return crypto.subtle.verify('HMAC', await pepperKey(env.STUDENT_PASSWORD_PEPPER), decode(credential.hash), await material(password, credential.salt, accountKey));
}

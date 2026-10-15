// Custom passwords are salted and stretched, then protected by a separate
// Worker secret. 100,000 is Workers' Web Crypto iteration cap.
// A separately encrypted copy supports the owner's private login-details view.
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

const COPY_SCHEME = 'aes-256-gcm-v1';
async function copyKey(env) {
  const secret = env.STUDENT_PASSWORD_ENCRYPTION_KEY;
  if (typeof secret !== 'string' || !/^[0-9a-f]{64}$/i.test(secret)) throw new Error('Private password storage is unavailable. Please try again later.');
  return crypto.subtle.importKey('raw', Uint8Array.from(secret.match(/../g), x => parseInt(x, 16)), 'AES-GCM', false, ['encrypt', 'decrypt']);
}
const copyContext = (accountKey, credential) => encoder.encode(JSON.stringify([COPY_SCHEME, accountKey, credential.scheme, credential.salt, credential.hash]));
export async function encryptStudentPassword(env, password, accountKey, credential) {
  const iv = crypto.getRandomValues(new Uint8Array(12));
  const ciphertext = await crypto.subtle.encrypt({ name:'AES-GCM', iv, additionalData:copyContext(accountKey, credential), tagLength:128 }, await copyKey(env), encoder.encode(normalized(password)));
  return { scheme:COPY_SCHEME, iv:encode(iv), ciphertext:encode(ciphertext) };
}
export async function decryptStudentPassword(env, copy, accountKey, credential) {
  try {
    if (copy?.scheme !== COPY_SCHEME || !credential) throw new Error('Invalid copy');
    const plaintext = await crypto.subtle.decrypt({ name:'AES-GCM', iv:decode(copy.iv), additionalData:copyContext(accountKey, credential), tagLength:128 }, await copyKey(env), decode(copy.ciphertext));
    return new TextDecoder().decode(plaintext);
  } catch { throw new Error('The saved password could not be opened. Please try again later.'); }
}

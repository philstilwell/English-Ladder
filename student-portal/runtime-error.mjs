// Only fixed diagnostic labels leave this function. Never log exception text,
// request URLs/bodies, account records, secrets, or session cookies.
export function runtimeErrorCategory(error) {
  const message = String(error?.message || '');
  for (const [category, pattern] of [
    ['daily_limit', /daily|free tier|free plan|quota/i],
    ['storage_full', /SQLITE_FULL|disk is full/i],
    ['cpu_limit', /CPU|exceeded.*resource/i],
    ['overloaded', /overload|too many requests/i],
    ['storage_timeout', /storage.*timeout/i],
    ['object_reset', /reset|replaced|invalidated/i],
    ['memory_limit', /memory limit/i],
    ['directory_binding', /^Directory unavailable$/],
    ['internal_error', /internal error/i],
    ['network_error', /network|connection/i],
  ]) if (pattern.test(message)) return category;
  return ['TypeError', 'ReferenceError', 'SyntaxError', 'RangeError'].includes(error?.name) ? error.name : 'unclassified';
}

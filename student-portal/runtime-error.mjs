// Only fixed diagnostic labels leave this function. Never log exception text,
// request URLs/bodies, account records, secrets, or session cookies.
export function runtimeErrorCategory(error) {
  const message = String(error?.message || '');
  if (/daily|per day|free tier|free plan|quota/i.test(message)) {
    if (/request/i.test(message)) return 'request_allowance';
    if (/read/i.test(message)) return 'read_allowance';
    if (/writ/i.test(message)) return 'write_allowance';
    if (/duration|compute|GB.?s/i.test(message)) return 'duration_allowance';
    if (/storage/i.test(message)) return 'storage_allowance';
    return /daily|per day/i.test(message) ? 'daily_limit' : 'plan_limit';
  }
  for (const [category, pattern] of [
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

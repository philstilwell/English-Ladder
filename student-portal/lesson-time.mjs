export function sessionId(startedAt, timeZone = 'America/New_York') {
  const parts = Object.fromEntries(new Intl.DateTimeFormat('en-US', { timeZone, year: 'numeric', month: '2-digit', day: '2-digit',
    hour: '2-digit', minute: '2-digit', hourCycle: 'h23' }).formatToParts(new Date(startedAt)).map(p => [p.type, p.value]));
  return `${parts.year}-${parts.month}-${parts.day}-${parts.hour}${parts.minute}`;
}

export function nextCalendarMonth(day) {
  const [year, month, date] = day.split('-').map(Number);
  const target = new Date(Date.UTC(year, month, 1));
  target.setUTCDate(Math.min(date, new Date(Date.UTC(year, month + 1, 0)).getUTCDate()));
  return target.toISOString().slice(0, 10);
}

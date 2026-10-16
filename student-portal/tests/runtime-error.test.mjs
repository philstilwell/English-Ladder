import test from 'node:test';
import assert from 'node:assert/strict';
import { runtimeErrorCategory } from '../runtime-error.mjs';

test('runtime diagnostics classify infrastructure failures without returning sensitive exception text',()=>{
  for (const [message,category] of [
    ['Daily limit exceeded','daily_limit'],
    ['Daily storage limit exceeded','storage_allowance'],
    ['Daily Durable Object requests limit exceeded','request_allowance'],
    ['Free plan rows read allowance exceeded','read_allowance'],
    ['Daily rows written allowance exceeded','write_allowance'],
    ['Daily duration allowance exceeded','duration_allowance'],
    ['Free plan quota exceeded','plan_limit'],
    ['database or disk is full: SQLITE_FULL','storage_full'],
    ['Exceeded CPU limit','cpu_limit'],
    ['Durable Object is overloaded','overloaded'],
    ['Durable Object storage operation exceeded timeout','storage_timeout'],
    ['Directory unavailable','directory_binding'],
    ['Private Person password=fictional-secret cookie=fictional-cookie','unclassified'],
  ]) assert.equal(runtimeErrorCategory(new Error(message)),category);
  assert.equal(runtimeErrorCategory(new TypeError('private student detail')),'TypeError');
});

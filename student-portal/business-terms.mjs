import bank from './business-terms-bank.json' with { type: 'json' };
import { createSelfCheckHandler } from './self-check.mjs';

export const handleBusinessTerms = createSelfCheckHandler('terms', bank);

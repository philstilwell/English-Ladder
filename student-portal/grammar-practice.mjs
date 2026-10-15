import bank from './grammar-bank.json' with { type: 'json' };
import { createSelfCheckHandler } from './self-check.mjs';

export const handleGrammarPractice = createSelfCheckHandler('grammar', bank);

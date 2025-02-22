# [보충] NestJS를 위한 VSCode 셋업 및 ESLint, Prettier

> https://eslint.org/docs/rules/

[TOC]

# ESLint

## 1. VSCode 확장 프로그램 'ESLint'를 설치한다.

## 2. `.eslintrc.js` 설정

```javascript
module.exports = {
  parser: '@typescript-eslint/parser',
  parserOptions: {
    project: 'tsconfig.json',
    tsconfigRootDir : __dirname, 
    sourceType: 'module',
  },
  plugins: ['@typescript-eslint/eslint-plugin'],
  extends: [
    'plugin:@typescript-eslint/recommended',
    'plugin:prettier/recommended',
  ],
  root: true,
  env: {
    node: true,
    jest: true,
  },
  ignorePatterns: ['.eslintrc.js'],
  rules: {
    // console.log 사용이 바람직한 것은 아니기 때문에 warn하도록 설정
    'no-console': 'warn',
    '@typescript-eslint/interface-name-prefix': 'off',
    '@typescript-eslint/explicit-function-return-type': 'off',
    '@typescript-eslint/explicit-module-boundary-types': 'off',
    '@typescript-eslint/no-explicit-any': 'off',
  },
};
```



# Prettier 설정

변경 X
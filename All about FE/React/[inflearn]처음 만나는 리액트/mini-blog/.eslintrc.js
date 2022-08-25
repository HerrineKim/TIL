module.exports = {
    root: true,
    env: {
        browser: true,
        amd: true,
        node: true,
    },
    extends: ["eslint:recommended", "plugin:react/recommended", "plugin:prettier/recommended"],
    overrides: [],
    parserOptions: {
        ecmaVersion: "latest",
        sourceType: "module",
    },
    plugins: ["react"],
    rules: {},
};

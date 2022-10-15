# yarnインストール時のトラブルシューティング

## 問題

以下のようなエラーが発生し、yarn addができない
``` js
yarn add v1.22.18
error Missing list of packages to add to your project.
info Visit https://yarnpkg.com/en/docs/cli/add for documentation about this command.
bot-todo@cbd4f3501aa4:/bot-todo$ yarn add @slack/bolt
yarn add v1.22.18
info No lockfile found.
[1/4] Resolving packages...
[2/4] Fetching packages...
[3/4] Linking dependencies...
error An unexpected error occurred: "EPERM: operation not permitted, copyfile '/home/bot-todo/.cache/yarn/v6/npm-@slack-oauth-2.5.4-94882a57068ae837720291ab875fe08d276ace77-integrity/node_modules/@slack/oauth/README.md' -> '/bot-todo/node_modules/@slack/oauth/README.md'".
info If you think this is a bug, please open a bug report with the information provided in "/bot-todo/yarn-error.log".
```

## 原因

WSL2の権限回りが問題である模様。具体的な情報は見当たらず
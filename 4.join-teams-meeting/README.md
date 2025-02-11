Init the project:
```shell
npm init -y

npm install @azure/communication-common --save
npm install @azure/communication-calling --save

npm install copy-webpack-plugin@^11.0.0 webpack@^5.88.2 webpack-cli@^5.1.4 webpack-dev-server@^4.15.1 --save-dev
```

To run the frontend:
```shell
npx webpack serve --config webpack.config.js
```
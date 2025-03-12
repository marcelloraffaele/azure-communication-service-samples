https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/voice-video-calling/getting-started-with-calling?tabs=uwp&pivots=platform-web

You need to:
1. Run the server
2. open in two different browsers
3. generate a token for each browser
4. call from one browser to another using the user id of the other browser
5. accept the call in the other browser

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
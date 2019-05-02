const webpack = require('webpack');
const path = require("path");
const isProd = process.env.NODE_ENV === "production";

module.exports = {
  publicPath: isProd ? "/static/" : "",
  outputDir: path.resolve(__dirname, "../britecore/templates"),
  assetsDir: "../../static/",
  configureWebpack: {
    plugins: [
      new webpack.optimize.LimitChunkCountPlugin({
        maxChunks: 6
      })
    ]
  },
  pwa: {
    name: 'Vue Dashboard',
    themeColor: '#172b4d',
    msTileColor: '#172b4d',
    appleMobileWebAppCapable: 'yes',
    appleMobileWebAppStatusBarStyle: '#172b4d'
  },
  css: {
    // Enable CSS source maps.
    sourceMap: process.env.NODE_ENV !== 'production'
  }
};
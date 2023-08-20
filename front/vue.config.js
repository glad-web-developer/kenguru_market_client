const { defineConfig } = require('@vue/cli-service')
// const path = require("path");
module.exports = defineConfig({
  transpileDependencies: true,
  // publicPath: '/static/front_prod/',
  outputDir: "../backend/kenguru",
  assetsDir: 'static/front_prod',
  indexPath: 'templates/index.html'

})

module.exports = {
  // Use relative publicPath in production for maximum compatibility
  publicPath: process.env.NODE_ENV === 'production' ? '/static/dist/' : '/',
  outputDir: '../static/dist', // Assuming your Django project's STATICFILES_DIRS is configured to include '../static'
  indexPath: '../../templates/_base_vue.html', // Adjust the path based on your Django templates structure

  configureWebpack: {
    // Configuration for development server
    devServer: {
      historyApiFallback: true,
      devMiddleware: {
        writeToDisk: true, // Necessary if Django serves your Vue app in development
      },
    },
  },
};

// You can uncomment and use the below configuration if you have specific dependencies that need to be transpiled
// const { defineConfig } = require('@vue/cli-service');
// module.exports = defineConfig({
//   transpileDependencies: true,
//   publicPath: process.env.NODE_ENV === 'production' ? '/static/dist/' : '/',
//   outputDir: '../static/dist',
//   indexPath: '../../templates/_base_vue.html',
//   configureWebpack: {
//     devServer: {
//       historyApiFallback: true,
//       devMiddleware: {
//         writeToDisk: true,
//       },
//     },
//   },
// });
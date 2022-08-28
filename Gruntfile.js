module.exports = function (grunt) {

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        autoprefixer: {
            dist: {
                src: 'css/styles.css',
                dest: 'assets/styleprefixer.css'
            }
        },
        cssmin: {
            target: {
                files: {
                    'css/styles.css': ['css/main.css', 'css/welcomeScreen.css', 'css/setDimension.css', 'css/game.css']
                }
            }
        },
    });
    grunt.loadNpmTasks('grunt-autoprefixer');
    grunt.loadNpmTasks('grunt-contrib-cssmin');
}
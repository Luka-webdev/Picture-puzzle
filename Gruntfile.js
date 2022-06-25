module.exports = function (grunt) {

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        autoprefixer: {
            dist: {
                src: 'css/style.css',
                dest: 'css/styleprefixer.css'
            }
        },
        cssmin: {
            target: {
                files: {
                    'css/styleprefixer.min.css': ['css/styleprefixer.css']
                }
            }
        },
    });
    grunt.loadNpmTasks('grunt-autoprefixer');
    grunt.loadNpmTasks('grunt-contrib-cssmin');
}
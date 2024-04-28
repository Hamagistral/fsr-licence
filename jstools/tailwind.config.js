module.exports = {
    future: {
        removeDeprecatedGapUtilities: true,
        purgeLayersByDefault: true,
    },
    purge: {
        enabled: false, //true for production build
        content: [
            '../**/templates/*.html',
            '../**/templates/**/*.html',
            './node_modules/flowbite/**/*.js'
        ]
    },
    theme: {
        extend: {},
    },
    variants: {},
    plugins: [
        require('flowbite/plugin')
    ],
}
const apiTestHandler = (payload, context, callback) => {
    callback(null, {
        statusCode: 200,
        body: JSON.stringify({
            message: 'Hello FromLambda'
        }),
    });
}
module.exports = {
    apiTestHandler,
}
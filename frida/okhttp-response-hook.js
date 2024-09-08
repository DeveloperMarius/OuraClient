Java.perform(function (){
    console.log("\n");
    var printed = [];
    var Buffer = Java.use('eq.i');//Java.use("okio.Buffer");
    var BufferSource = Java.use('eq.k');//Java.use("okio.BufferSource");
    var BufferSink = Java.use('eq.j');//Java.use("okio.BufferSink");
    var Response = Java.use('okhttp3.Response');

    var ResponseConstructor = Response.$init.overload('okhttp3.Request', 'okhttp3.Protocol', 'java.lang.String', 'int', 'okhttp3.Handshake', 'okhttp3.Headers', 'okhttp3.ResponseBody', 'okhttp3.Response', 'okhttp3.Response', 'okhttp3.Response', 'long', 'long', 'okhttp3.internal.connection.Exchange');
    ResponseConstructor.implementation = function (request, protocol, message, code, handshake, headers, responseBody, networkResponse, cacheResponse, priorResponse, sentRequestAtMillis, receivedResponseAtMillis, exchange) {
        var response = ResponseConstructor.call(this, request, protocol, message, code, handshake, headers, responseBody, networkResponse, cacheResponse, priorResponse, sentRequestAtMillis, receivedResponseAtMillis, exchange);
        //Check if request was already printed or if response body is null
        var requestTraceId = headers.values('x-trace-id').get(0);
        if(responseBody === null || printed.indexOf(requestTraceId) !== -1)
            return response;
        //Read Response Body
        var responseContentLength = responseBody.contentLength();
        var responseBodyContent = null;
        try {
            //"Peek" the response body so that it can be read again.
            //Cannot use response.peekBody() because Response object
            //seems to be always undefined when constructed here.
            //Thus is code replicates the peekBody() method.
            var responsePeek = responseBody.source().peek();
            var responseBuffer = Buffer.$new();
            responsePeek.k(responseContentLength);
            //min = Math.min(responseContentLength, Long.MAX_INTEGER);
            var min = responseContentLength;
            while (min > 0) {
                var read = responsePeek.read(responseBuffer, min);
                if (read == -1) {
                    throw new Error("EOFException");
                }
                min -= read;
            }
            responseBodyContent = responseBuffer.t();//buffer.readUtf8();
        } catch (e) {
            //Sometimes the body is read before the response is constructed.
            //It is not clear why, but in this case an IllegalStateException
            //is thrown and the body cannot be read.
        }
        if(responseBodyContent === null)
            return response;
        //Print Request and Response
        printed.push(requestTraceId);
        var out = "";
        out += "-----------------------------------------\n"
        //Print Request
        out += "[Request]:\n";
        out += request.method() + " " + request.url() + "\n";
        for (var i = 0; i < request.headers().size(); i++) {
            out += request.headers().name(i) + ": " + request.headers().value(i) + "\n";
        }
        var requestBody = request.body();
        var contentLength = requestBody ? requestBody.contentLength() : 0;
        if (contentLength > 0) {
            var buffer = Buffer.$new();
            requestBody.writeTo(buffer);
            out += "\n" + buffer.t() + "\n";//buffer.readUtf8();
        }
        //Print Response
        out += "\n[Response]: " + code + "\n";
        for (var i = 0; i < headers.size(); i++) {
            out += headers.name(i) + ": " + headers.value(i) + "\n";
        }
        out += "\n" + responseBodyContent + "\n";
        out += "-----------------------------------------";
        console.log(out);

        return response;
    }
});

Java.perform(function () {
    var sp = Java.use("android.app.SharedPreferencesImpl$EditorImpl");
    sp.putString.implementation = function (key, value) {
        console.log(`putString("${key}", "${value}")`);

        let outer = this.this$0.value; // SharedPreferencesImpl
        console.log("pref file: " + outer.mFile.value);

        return this.putString(key, value);
    }
    sp.getString.implementation = function (key, value) {
        console.log(`getString("${key}", "${value}")`);

        let outer = this.this$0.value; // SharedPreferencesImpl
        console.log("pref file: " + outer.mFile.value);

        var ret = this.getString(key, value);
        console.log(`returning: ${ret}`);
        return ret;
    }
});
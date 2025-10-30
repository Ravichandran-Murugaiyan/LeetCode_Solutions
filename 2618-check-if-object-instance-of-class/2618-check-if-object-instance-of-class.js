/**
 * @param {any} obj
 * @param {any} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function(obj, classFunction) {
    if (obj === null || obj === undefined || typeof classFunction !== 'function') {
        return false;
    }

    const proto = Object.getPrototypeOf(Object(obj));

    let currentProto = proto;
    while (currentProto) {
        if (currentProto === classFunction.prototype) {
            return true;
        }
        currentProto = Object.getPrototypeOf(currentProto);
    }
    return false;
};

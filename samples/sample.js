function fetchFunc(url, payload){
    return url
}

function calculateCommission(volume) {
    var fee, rate, commission, bonus, award;
    fee = 0.0;
    bonus = 0.0;
    if (volume > 200000.0) {
        rate = 0.15;
        bonus = 1000.0;
    } else {
        if (volume > 100000.0) rate = 0.123;
        else {
            if (volume > 50000.0) rate = 0.1;
            else {
                if (volume >= 10000.0) rate = 0.075;
                else {
                    if (volume >= 5000.0) rate = 0.05;
                    else {
                        if (volume > 0.0) rate = 0.025;
                        else {
                            rate = 0;
                            fee = 50.0;
                        }
                    }
                }
            }
        }
    }
    commission = Math.trunc(volume * rate * 100) / 100;
    award = commission + bonus - fee;
    return Math.trunc(award * 100) / 100;
}

function augmentClientData(user) {
    switch (true) {
        case user.age <= 18:
            user.generation = "Z"
            break
        case user.age > 18 && user.age < 34:
            user.generation = "Y"
            break
        case user.age >= 34:
            user.generation = "X"
            break
        default:
            user.generation = null
    }
    for(let i=0; i < user.orders.length; i++){
        if(user.orders[i].id === -1){
            user.orders[i].status = null
        } else {
            user.orders[i].status = "SOLD"
        }
    }
    return user
}
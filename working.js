let receipt_items = ["apple", "orange", "beef"];

class Product {
    constructor(name, vegan, locallySourced, price) {
        this.name = name;
        this.vegan = vegan;
        this.locallySourced = locallySourced;
        this.price = price;
    }

    
    displayInfo() {
        console.log(`Product: ${this.name}`);
        console.log(`Vegan: ${this.vegan ? 'Yes' : 'No'}`);
        console.log(`Locally Sourced: ${this.locallySourced ? 'Yes' : 'No'}`);
        console.log(`Price: $${this.price}`);
    }
}


const apple = new Product("apple", true, true, 2.00);
const orange = new Product("orange", true, false, 2.00);
const beef= new Product("beef", false, false, 2.00);

let database = [apple,orange,beef];

function getIndexOfInstance(variable, instanceList) {
    for (let i = 0; i < instanceList.length; i++) {
        if (variable === instanceList[i].name) {
            return i;
        }
    }
    return -1; // Return -1 if the variable doesn't match any instance name
}

function itemScore(product){
    let score = 0
    if (product.vegan){
        score += 20
    }
    if (product.locallySourced){
        score += 10
        }
    return score;
}

function receiptScore(receipt_items) {
    let score = 0; 
    for (let i = 0; i < receipt_items.length; i++) {
        const productIndex = getIndexOfInstance(receipt_items[i], database);
        if (productIndex !== -1) { 
            const product = database[productIndex];
            if (product) { // 
                score += itemScore(product); 
            } else {
                console.log(`Product '${receipt_items[i]}' not found in the database.`);
            }
        } else {
            console.log(`Product '${receipt_items[i]}' not found in the database.`);
        }
    }
    return score;
}

console.log(receiptScore(receipt_items))




    

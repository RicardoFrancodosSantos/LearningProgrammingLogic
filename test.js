function returnFalse()
{
    console.log ("i am false")
    return false;
}

function returnTrue()
{
    console.log ("i am true")
    return true;
}

const result = returnFalse() && returnTrue();


console.log("result is: " + result)
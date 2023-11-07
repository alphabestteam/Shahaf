function sequenceA() {
    setTimeout(_ => console.log('Sponge'), 0);
    console.log("Bob");
}

function sequenceB(){
    setTimeout(_ => console.log(`🍅 Timeout at B`), 0);
    Promise.resolve().then(_ => console.log('🍍 Promise at B'));
}

function sequenceC(){
    setTimeout(_ => console.log(`🍅 Timeout at C`), 0);
    Promise.resolve().then(_ => setTimeout(console.log('🍍 Promise at C'), 1000));
}

function sequenceD(){
    console.log('Sponge');
    setTimeout(_ => console.log('Square'), 0);
    Promise.resolve().then(_ => console.log('Pants'));
    console.log('Bob');
}

function questionA(){
    sequenceA();
}

function questionB(){
    sequenceB();
}

function questionC(){
    sequenceC();
}

function questionD(){
    sequenceD();
}

function questionE(){
    sequenceB();
    sequenceC();
}

//questionA();

//the sequence of printing is bob ans than sponge
// bob is first because sponge is in time out which takes it out of the function execution stack and put it last

//questionB();

//the promise is printed first because promise is the first function to be in the job queue

//questionC();

//the promise is printed first because even though it has bigger time out js executes promises first
//and because it is single threaded it waited for the timeout of the promise to end and then moves on to other tasks

//questionD();

//it prints sponge then bob then pants then square
//the order is this way because js executes the synchronic things (static things like console log)
//then the promise is executed and lat one the timeout

//questionE();

//js reads all the tasks he has to do and than reorganize them in the correct way
//promise has a priority on timeout
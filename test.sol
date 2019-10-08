
//adress 0x2f60989b156B60Ad388377D636a5b4D8E426476d
pragma solidity ^0.5.11;

contract Sample_New {
    uint a;
    uint b;
    uint c;
    uint d;
    uint check = 0;

    function get() public returns (uint) {
        a = a+1;
        return a;
    }
    function get2() public returns (uint) {
        b = b+1;
        return b;
    }
    function get3() public returns (uint) {
        c = c+1;
        return c;
    }
    function get4() public returns (uint) {
        d = d+1;
        return d;
    }
    function clear() public {
        check++;
        clear_2();
    }
    function clear_2()private{
            if(check == 2)
            {
                a = 0;
                b = 0;
                c = 0;
                d = 0;
                check = 0;
            }
    }
    function result_1() public view returns(uint){
        return a;
    }
    function result_2() public view returns(uint){
        return b;
    }
    function result_3() public view returns(uint){
        return c;
    }
    function result_4() public view returns(uint){
        return d;
    }
}

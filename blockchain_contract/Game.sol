pragma solidity ^0.4.18;

contract Sample {
    uint data = 5;

    function set(uint d) public{
        data = d;
    }

    function get() public constant returns (uint retVal) {
        return data;
    }
}

pragma solidity ^0.4.18;

contract Sample_New {
    uint a=2;
    uint b;

    function get() public returns (uint) {
        a = a+1;
        return a;
    }
    function get2() public returns (uint) {
        b = b+1;
        return b;
    }
    function result() public constant returns(uint){
        return (a,b);
    }
}

//Main code  address   0xfA6FB40eFE9e66eb82bCB44392f722EDF4C9B70C
pragma solidity ^0.4.18;

contract Sample_New {
    uint a;
    uint b;

    function get() public returns (uint) {
        a = a+1;
        return a;
    }
    function get2() public returns (uint) {
        b = b+1;
        return b;
    }
    function result_1() public constant returns(uint){
        return a;
    }
    function result_2() public constant returns(uint){
        return b;
    }
}

//SPDX-License-Identifier:MIT
pragma solidity >=0.4.0<=0.9.0;

contract StudentRegister{

    address public owner;
  
    mapping (address=>student)students;
    
    constructor() {
        owner=msg.sender;
    }
    struct student{
        
        address studentId;
        string  name;
        string course;  
    }
    
    function register(address studentId,string memory name,string memory course) public {
            
            students[studentId]=student(studentId,name,course);
    }
            
    function getStudentDetails(address studentId) public view returns (address,string memory,string memory){

        return(students[studentId].studentId,students[studentId].name,students[studentId].course);
    }
      receive() external payable {}
}

Feature: Data processing calls
	As a Data processing engine
		It will release daily Data Processing Job
		It will be able to work with Data Lake


	Scenario Outline: Data Processing Job
		When I input dataIn=<dataIn>
		And do action=<action>
		Then we will have succeeded dataOut=<dataOut>
		Examples:
			|dataIn |action  |dataOut  |
			|data1  |action1 |dataOut1 |
			|data1  |action2 |dataOut2 |
			|data1  |action3 |dataOut3 |

			|data2  |action1 |dataOut4 |
			|data2  |action2 |dataOut5 |
			|data2  |action3 |dataOut6 |

			|data3  |action1 |dataOut7 |
			|data3  |action2 |dataOut8 |
			|data3  |action3 |dataOut9 |


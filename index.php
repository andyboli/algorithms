<!-- 
Create a hashmap (or a simple object in PHP) that contains the elementary functions of addition, subtraction, multiplication, and division.
Take into account that the division must not allow 0 dividend
The sum function allows an array as an input parameter and adds all its elements.
The subtraction function allows an array as an input parameter and subtracts all its elements.
Multiplication Function - Ditto
The division function accepts two parameters: a and b.
 -->
<?php
$addition = function (array $arr) {
    echo array_sum($arr);
};

$change_value = function ($value) {
    return $value * -1;
};

$subtraction = function (array $arr) {
    $sub = 0;
    for ($i = 0; $i <= count($arr); $i++) {
        $sub -= array_search($i, $arr);
    }
    echo $sub;
};

$multiplication = function (array $arr) {
    echo array_product($arr);
};

$division = function ($num1, $num2) {
    if ($num2 == 0)
        echo "cannt make a zero division";
    else
        echo $num1 / $num2;
};

$array = array(
    "addition" => $addition,
    "subtraction" => $subtraction,
    "multiplication" => $multiplication,
    "division" => $division,
);

$array["subtraction"]([1, 2, 3, 3, 4])

    ?>
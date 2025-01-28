
    /*     let d = "-100";
        let e = "20"
        let f = 30;
        let g = true;
        console.log(-+d + ++f + ++e * ++g); */
    console.log(10 * 20 * 15 % 3 * 190 * 10 * 400); // 0
    // console.log(10 * 20 + 15 % 3 + 190 + 10 - 400) 
    let num = 3;
    // Solution One
    console.log(num + (true * num)); // 6

    // Solution Two
    console.log(true + true + true + num); // 6

    // Soultion Three
    console.log(num + num); // 6

    // Soultion Four
    console.log(num * --num); // 6

    // Solution Five
    console.log(num * (true + true)); // 6

    // Solution Six
    console.log(++num + true + true); // 6

    let num2 = "10";

    // Solution One
    console.log(+num2 + +num2); // 20

    // Solution Two

    console.log(+num2 + --num2 + --num2 - --num2); // 20
    // Solution Three
    console.log(--num2 * --num2 - +num2 - +num2); // 20

    // Solution Four
    console.log(+num2 * +num2 - +num2); // 20

    let points = 10;

    // Write Your Code Here
    /*     ++points
        ++points
        ++points */
    points += true + true + true
    console.log(points); // 13

    // Write Your Code Here
    /*     --points
        --points
        --points
        --points
        --points */
    points -= true + true + true + true + true

    console.log(points); // 8;


// alert( 1.35.toFixed(1) ); // 1.4
// In the similar example below, why is 6.35 rounded to 6.3, not 6.4?

// alert( 6.35.toFixed(1) ); // 6.3
// How to round 6.35 the right way? 

alert( (6.35 * 10).toFixed(20) );
alert( Math.round(6.35 * 10) / 10 );
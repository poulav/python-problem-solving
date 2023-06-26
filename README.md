# Python Problem Solving

<h2>Roman to Integer</h2>
Problem Statement - Convert any given roman number to its equivalent integer.

My thought process
<ul>
    <li>I have used the index of list to find if the value of a roman digit is greater or smaller than the next. Index list was arranged in the order such that higher index refers to higher valued roman number letter.</li>
    <li>I have used dictionary to store the values with respect to roman letters, example, I refers to 1, X refers to 10, and so on.</li>
    <li>I have used a counter to get the next roman digit value with respect to the current inside the for loop (it is looping through the list/roman letter set).</li>
</ul>

<strong>Breakdown using my friend Chat GPT:</strong>
<ul>
  <li>The code defines a class called <code>Solution</code>.</li>
  <li>The class contains a method named <code>romanToInt</code> that takes a string <code>s</code> as input and returns an integer.</li>
  <li>It initializes <code>romanNumberSystem</code>, a list of Roman numeral characters in descending order: <code>['I', 'V', 'X', 'L', 'C', 'D', 'M']</code>.</li>
  <li>It initializes <code>romanToInteger</code>, a dictionary that maps each Roman numeral character to its corresponding integer value.</li>
  <li>It initializes <code>sumOfNumbers</code> to 0, which will store the final integer value.</li>
  <li>It calculates the length of the input string <code>s</code> and initializes a counter variable to keep track of the current position.</li>
  <li>It enters a loop that iterates through each character <code>currentCharacter</code> in the input string.</li>
  <li>Inside the loop, it checks if there is a next character available by comparing the counter with the length of the string.</li>
  <li>If a next character exists, it is assigned to <code>nextCharacter</code>; otherwise, it is set to an empty string.</li>
  <li>It keeps track of the previous character's position in the string using the <code>lastCounter</code> variable.</li>
  <li>It performs checks to determine the appropriate conversion for the current character:</li>
  <ul>
    <li>If the length of the string is greater than 1 and the next character is not an empty string, it compares the positions of the current and next characters in the <code>romanNumberSystem</code> list.</li>
    <ul>
      <li>If the next character has a higher index, it subtracts the integer value of the current character from the integer value of the next character and adds the result to <code>sumOfNumbers</code>.</li>
    </ul>
    <li>If the previous counter is greater than -1 and the position of the previous character in <code>romanNumberSystem</code> is less than the position of the current character, it increments the counter and continues to the next iteration of the loop without adding the current character to <code>sumOfNumbers</code>.</li>
    <li>If none of the above conditions are met, it adds the integer value of the current character directly to <code>sumOfNumbers</code>.</li>
  </ul>
  <li>After processing each character, the loop advances the counter.</li>
  <li>Once all characters have been processed, the method returns the accumulated value in <code>sumOfNumbers</code>.</li>
  <li>The code then assigns the string "D" to the variable <code>s</code>.</li>
  <li>It creates an instance of the <code>Solution</code> class called <code>objSolution</code>.</li>
  <li>It calls the <code>romanToInt</code> method on <code>objSolution</code> with <code>s</code> as the argument and assigns the returned value to <code>ret</code>.</li>
  <li>Finally, it prints the value of <code>ret</code> to the console.</li>
</ul>


<hr/>
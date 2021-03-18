## CSS

### How to do selectors
```css
div.red.green /* select div with class of red and green */
span, li /* spans and li are selected */
ul li /* select li inside of a ul, even if it grand children */
ul > li /* select li that is direct child of ul */
li.red ~ li /* select li that comes after li with class red */
li.red + li /* select just the li that is directly after li with class red
```
### nth element selectors
```css
li.red:first-child /* select the very first child that is li with .red (must be first)*/
li:nth-child()
```
### Box Sizing
css box sizing - border box (account for border and padding etc when specifying sizes)
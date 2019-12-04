Simple Button Example:

```js
<Button text="Action" clickHandler={() => alert('Click!')} />
```

Angry Button Example:

```js
<Button
  className="bg-danger"
  text="Action"
  clickHandler={() => alert("I'm angry!")}
/>
```

Custom Color Example:

```js
<Button
  className="force-button"
  text="Action"
  clickHandler={() => alert("I'm a custom color!")}
/>
```

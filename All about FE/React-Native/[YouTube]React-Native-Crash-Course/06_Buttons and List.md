# 06_Buttons and List



## List item Delete 구현하기



### `GoalItem.js`

```react
import React from "react";
import { StyleSheet, View, Text, Pressable } from "react-native";

function GoalItem(props) {
  return (
    <Pressable onPress={props.onDeleteItem.bind(this, props.id)}>
      <View style={styles.goalItem}>
        <Text style={styles.goalText}>{props.text}</Text>
      </View>
    </Pressable>
  );
}
```



### `App.js`

```react
            return (
              <GoalItem
                text={itemData.item.text}
                id={itemData.item.id}
                onDeleteItem={deleteGoalHandler}
              />
```



### `.bind()` 함수

https://ko.javascript.info/bind

> 객체 메서드가 객체 내부가 아닌 다른 곳에 전달되어 호출되면 `this` 정보가 사라지는 문제를 해결해준다.



#### 구문

```javascript
    func.bind(thisArg[, arg1[, arg2[, ...]]])
```



#### 예문

```javascript
let user = {
  firstName: "John",
  sayHi() {
    alert(`Hello, ${this.firstName}!`);
  }
};

let sayHi = user.sayHi.bind(user); // (*)

// 이제 객체 없이도 객체 메서드를 호출할 수 있습니다.
sayHi(); // Hello, John!

setTimeout(sayHi, 1000); // Hello, John!

// 1초 이내에 user 값이 변화해도
// sayHi는 기존 값을 사용합니다.
user = {
  sayHi() { alert("또 다른 사용자!"); }
};
```


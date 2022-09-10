# 04_Handling events

- 버튼 클릭: `onPress={}`

## State와 Event handling

1. `import { useState } from "react";`

2. state 선언 (` const [enteredGoalText, setEnteredGoalText] = useState("");`)

3. 함수 적용

   ```react
     function goalInputHandler(enteredText) {
       setEnteredGoalText(enteredText);
     }
   ```

   *기존의 state 값을 염두에 두어야 하는 함수의 경우에는 arrow function으로 표현한다.

   ```react
     function addGoalHandler() {
       setCourseGoals((currentCourseGoals) => [...currentGoals, enteredGoalText]);
     }
   ```

4. 리스트 출력

   ```react
         <View style={styles.goalsContainer}>
           {courseGoals.map((goal) => (
             <Text key={goal}>{goal}</Text>
           ))}
         </View>
   ```

   - key를 지정하지 않으면 에러를 띄운다.



### 코드

```react
import {
  StyleSheet,
  Text,
  View,
  Button,
  TextInput,
  ScrollView,
} from "react-native";
import React from "react";
import { useState } from "react";

export default function App() {
  const [enteredGoalText, setEnteredGoalText] = useState("");
  const [courseGoals, setCourseGoals] = useState([]);

  function goalInputHandler(enteredText) {
    setEnteredGoalText(enteredText);
  }

  function addGoalHandler() {
    setCourseGoals((currentCourseGoals) => [
      ...currentCourseGoals,
      enteredGoalText,
    ]);
  }

  return (
    <View style={styles.appContainer}>
      <View style={styles.inputContainer}>
        <TextInput
          style={styles.textInput}
          placeholder="Your course goal!"
          onChangeText={goalInputHandler}
        />
        <Button title="ADD" onPress={addGoalHandler} />
      </View>
      <ScrollView style={styles.goalsContainer}>
        {courseGoals.map((goal) => (
          <Text style={styles.goalItem} key={goal}>
            {goal}
          </Text>
        ))}
      </ScrollView>
    </View>
  );
}

const styles = StyleSheet.create({
  appContainer: {
    flex: 1,
    paddingTop: 50,
    paddingHorizontal: 16,
  },
  inputContainer: {
    flex: 1,
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center",
    marginBottom: 24,
    borderBottomWidth: 1,
    borderBottomColor: "#ccc",
  },
  textInput: {
    borderWidth: 1,
    borderColor: "black",
    width: "80%",
    marginRight: 8,
    padding: 8,
  },
  goalsContainer: {
    flex: 4,
  },
  goalItem: {
    margin: 8,
    padding: 8,
    borderRadius: 6,
    backgroundColor: "#5e0acc",
  },
});

```



### 결과

![image-20220910232815104](04_Handling%20events.assets/image-20220910232815104.png)



## ScrollView와 FlatList

> 컴포넌트별로 Android, iOS 각각 가능한 props 요소들이 있다,



### ScrollView

렌더를 한 번에 처리하기 때문에, 처리해야 할 데이터 양이 적은 경우에만 사용한다.



### FlatList

모든 데이터를 한 번에 렌더링하지 않고, 화면에 보여지는 부분만큼만 보이게 한다. 데이터의 양이 가변적일 때 사용하기 좋다.

##### 코드

```react
```


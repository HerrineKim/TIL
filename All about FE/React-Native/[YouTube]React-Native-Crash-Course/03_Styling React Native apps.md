# 03_Styling React Native apps

> CSS와 문법 유사하지만, 완전히 같지는 않다.



## 1.Inline Style

![image-20220910200908934](03_Styling%20React%20Native%20apps.assets/image-20220910200908934.png)



## 2. Style sheet

![image-20220910201000255](03_Styling%20React%20Native%20apps.assets/image-20220910201000255.png)



#### Style sheet의 장점

1. 스타일 요소 자동 완성 제공
2. validation 제공



## 전체 코드

```react
import { StyleSheet, Text, View, Button } from "react-native";
import React from "react";

export default function App() {
  return (
    <View style={styles.container}>
      <View>
        <Text style={styles.dummyText}>Another piece of text!</Text>
      </View>
      <Text
        style={{
          margin: 16,
          borderWidth: 2,
          borderColor: "red",
          padding: 16,
        }}
      >
        Open up App.js to start working on your app!
      </Text>
      <Button title="Tap me!" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
  },
  dummyText: {
    margin: 16,
    borderWidth: 2,
    borderColor: "red",
    padding: 16,
  },
});
```



## Layouts & Flexbox

> Flexbox는 react native에서 매우 중요하다. 이는 기존 CSS Flexbox와 매우 유사하다. 



### TextInput, Button, Text 배치하기

#### 코드

```react
import { StyleSheet, Text, View, Button, TextInput } from "react-native";
import React from "react";

export default function App() {
  return (
    <View style={styles.appContainer}>
      <View style={styles.inputContainer}>
        <TextInput placeholder="Your course goal!" />
        <Button title="ADD" />
      </View>
      <View>
        <Text>List of Goals</Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  appContainer: {
    padding: 50,
  },
  inputContainer: {
    flexDirection: "row",
    justifyContent: "space-between",
  },
  testInput: {
    borderWidth: 1,
    borderColor: "black",
    width: "80%",
    marginRight: 8,
    padding: 8,
  },
});
```

![image-20220910203311493](03_Styling%20React%20Native%20apps.assets/image-20220910203311493.png)



## Improving Layout

### Flexbox와 CSS를 사용해 레이아웃 개선하기



![image-20220910231136593](03_Styling%20React%20Native%20apps.assets/image-20220910231136593.png)

```react
import { StyleSheet, Text, View, Button, TextInput } from "react-native";
import React from "react";

export default function App() {
  return (
    <View style={styles.appContainer}>
      <View style={styles.inputContainer}>
        <TextInput style={styles.textInput} placeholder="Your course goal!" />
        <Button title="ADD" />
      </View>
      <View style={styles.goalsContainer}>
        <Text>List of Goals</Text>
      </View>
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
});

```




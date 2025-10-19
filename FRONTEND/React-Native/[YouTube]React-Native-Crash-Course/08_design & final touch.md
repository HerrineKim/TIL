# 08_design & final touch

## 고정 배경색 설정하는 법

![image-20220911200042042](07_design%20&%20final%20touch.assets/image-20220911200042042.png)



## 상태바 설정

1. `import { statusBar } from "expo-status-bar";`
2. ` <StatusBar style="light" />`



## `App.js`

```react
import {
  StyleSheet,
  // Text,
  View,
  Button,
  // TextInput,
  // ScrollView,
  FlatList,
} from "react-native";
import { StatusBar } from "expo-status-bar";
import React from "react";
import { useState } from "react";
import GoalItem from "./components/GoalItem";
import GoalInput from "./components/GoalInput";

export default function App() {
  const [modalIsVisible, setModalIsVisible] = useState(false);
  const [courseGoals, setCourseGoals] = useState([]);

  function startAddGoalHandler() {
    setModalIsVisible(true);
  }

  function endAddGoalHandler() {
    setModalIsVisible(false);
  }

  function addGoalHandler(enteredGoalText) {
    setCourseGoals((currentCourseGoals) => [
      ...currentCourseGoals,
      { text: enteredGoalText, id: Math.random().toString() },
    ]);
    endAddGoalHandler();
  }

  function deleteGoalHandler(id) {
    setCourseGoals((currentCourseGoals) => {
      return currentCourseGoals.filter((goal) => goal.id !== id);
    });
  }

  return (
    <>
      <StatusBar style="light" />
      <View style={styles.appContainer}>
        <Button
          title="Add New Goal"
          color="#5e0acc"
          onPress={startAddGoalHandler}
        />
        <GoalInput
          visible={modalIsVisible}
          onAddGoal={addGoalHandler}
          onCancel={endAddGoalHandler}
        />
        <View style={styles.goalsContainer}>
          <FlatList
            data={courseGoals}
            renderItem={(itemData) => {
              return (
                <GoalItem
                  text={itemData.item.text}
                  id={itemData.item.id}
                  onDeleteItem={deleteGoalHandler}
                />
              );
            }}
            keyExtractor={(item, index) => item.itemData}
            alwaysBounceVertical={false}
          />
        </View>
      </View>
    </>
  );
}

const styles = StyleSheet.create({
  appContainer: {
    flex: 1,
    paddingTop: 50,
    paddingHorizontal: 16,
    backgroundColor: "#1e085a",
  },
  goalsContainer: {
    flex: 4,
  },
});

```



## 최종 앱 화면(Android, iOS)

![image-20220911202114272](07_design%20&%20final%20touch.assets/image-20220911202114272.png)

![image-20220911200714958](07_design%20&%20final%20touch.assets/image-20220911200714958.png)

![image-20220911200756036](07_design%20&%20final%20touch.assets/image-20220911200756036.png)
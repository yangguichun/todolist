<template>
  <div>
    <BaseInputText v-model="newTodoText" placeholder="New todo" @keydown.enter="addTodo"/>
    <ul v-if="todos.length">
      <TodoListItem v-for="todo in todos" :key="todo.id" :todo="todo" @remove="removeTodo"/>
    </ul>
    <p v-else>Nothing left in the list. Add a new todo in the input above.</p>
  </div>
</template>

<script>
import BaseInputText from "./BaseInputText.vue";
import TodoListItem from "./TodoListItem.vue";

let nextTodoId = 1;

export default {
  components: {
    BaseInputText,
    TodoListItem
  },
  created: function() {
    this.$http.get("/gettodolist").then(
      response => {
        console.log("request success from backend", response.data);
        this.todos = response.data.list;
      },
      response => {
        console.log("request fail from backend", response.data);
      }
    );
  },
  data() {
    return {
      newTodoText: "",
      todos: [
      ]
    };
  },
  methods: {
    addTodo() {
      const trimmedText = this.newTodoText.trim();
      if (trimmedText) {
        this.$http
          .post("/add", {
            title: trimmedText
          })
          .then(
            response => {
              console.log("add item sucess to backend");
              console.log(response.data)
              console.log(response.data.id)
              this.todos.push({
                id: response.data.id,
                title: trimmedText,
                createTime: new Date()
              });
              this.newTodoText = "";
            },
            response => {
              console.log("add item failed to backend", response.json);
            }
          );
      }
    },
    removeTodo(idToRemove) {
      // console.log(idToRemove)
      // for(let item of this.todos){
      // 	console.log(item)
      // 	if (item.id == idToRemove){
      // 		this.todos.push({
      // 			id: 10,
      // 			text:'34j3i4j3i4'
      // 		})
      // 	}
      // }
      // this.todos.shift()
      // this.todos.push({
      // 		id: 10,
      // 		text:'34j3i4j3i4'
      // })
      let url = "/del/" + idToRemove;
      this.$http.get(url).then(
        response => {
          console.log("del todo item success from backend", response.data);
        },
        response => {
          console.log("del todo item fail from backend", response.data);
        }
      );
      this.todos = this.todos.filter(todo => {
        return todo.id !== idToRemove;
      });
    }
  }
};
</script>
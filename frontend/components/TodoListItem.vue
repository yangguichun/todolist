<template>
  <li>
    {{ todo.title }}, {{ createTime}}
    <button @click="$emit('remove', todo.id)">
      X
    </button>
  </li>
</template>

<script>
export default {
  props: {
    todo: {
      type: Object,
      required: true
    }
  },
  computed:{
    createTime: function(){
      let date = new Date(this.todo.createTime)
      var y = date.getFullYear();  
      var m = date.getMonth() + 1;  
      m = m < 10 ? ('0' + m) : m;  
      var d = date.getDate();  
      d = d < 10 ? ('0' + d) : d;  
      var h = date.getHours();  
      var minute = date.getMinutes();  
      minute = minute < 10 ? ('0' + minute) : minute;  
      return y + '-' + m + '-' + d+' '+h+':'+minute;  
    }
  }
}
</script>
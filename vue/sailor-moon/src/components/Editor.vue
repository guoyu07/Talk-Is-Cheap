<template>
  <div>
    <div id="mark">
      <!--<textarea :value="input" debounce="300" @input="update"></textarea>-->
      <!--<div v-html="input"></div>-->
    </div>
    <div id="editor" style="width: 50%; height: 980px;"></div>
  </div>
</template>

<script>
// const ace = require('brace');
// require('brace/mode/javascript');
// require('brace/theme/monokai');
import * as ace from 'brace';
import 'brace/mode/javascript';
import 'brace/theme/terminal';

export default {
  name: 'editor',
  data() {
    return {
      input: 'editor',
    };
  },
  mounted() {
    const editor = ace.edit('editor');
    editor.getSession().setMode('ace/mode/javascript');
    editor.setTheme('ace/theme/terminal');
  },
  //methods: {
  //  update: (e) => {
  //    this.input = e.target.value;
  //  },
  //},
};
</script>

<style scoped>
#mark, body, html {
  margin: 0;
  height: 100%;
  font-family: Arial,sans-serif;
  color: #333;
}

textarea {
  border: none;
  border-right: 1px solid #ccc;
  resize: none;
  outline: none;
  background-color: #f6f6f6;
  font-size: 15px;
  font-family: courier,monospace;
  padding: 20px;
  min-height: 900px;
}

#mark div, textarea {
  display: inline-block;
  width: 49%;
  height: 100%;
  vertical-align: top;
  box-sizing: border-box;
  padding: 20px 20px;
}
</style>

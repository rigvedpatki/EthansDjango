<template>
  <b-container>
    <b-card header="Polls Application" title="List of Questions : " class="m-5" bg-variant="light">
      <b-list-group v-if="listOfQuestions">
        <b-list-group-item v-for=" question in listOfQuestions" :key="question.id" :href="'question/'+question.id">{{question.question_text}}</b-list-group-item>
      </b-list-group>
      <br>
      <br>
      <b-button href="question/" variant="primary"> Add new question</b-button>
    </b-card>
  </b-container>
</template>
<script>
import axios from 'axios'
import { questions } from '../configurations/developmentApi'
export default {
  name: 'Index',
  data() {
    return {
      listOfQuestions: []
    }
  },
  methods: {},
  created() {
    axios
      .get(questions)
      .then(response => {
        this.listOfQuestions = response.data
        this.listOfQuestions.sort((a, b) => {
          return new Date(a.pub_date) - new Date(b.pub_date)
        })
      })
      .catch(error => {
        console.log(error)
      })
  }
}
</script>

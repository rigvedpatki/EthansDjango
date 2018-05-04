<template>
  <b-container>
    <b-card :header="'Published on '+ question.pub_date.toLocaleString()" :title="question.question_text" class="m-5" bg-variant="light">
      <b-form-group label="Options">
        <b-form-radio-group v-model="selectedOption" :options="radioOptions" stacked></b-form-radio-group>
      </b-form-group>
      <br>
      <br>
      <b-button variant="primary" @click="vote" :disabled="isSelected"> Vote </b-button>
    </b-card>

    <div v-show="showResult">
      <b-card header="Result" class="m-5" bg-variant="light">
        <b-table striped hover :items="items"></b-table>
      </b-card>
    </div>
  </b-container>
</template>
<script>
import axios from 'axios'
import {
  questions,
  optionSearch,
  options
} from '../configurations/developmentApi'
export default {
  name: 'Question',
  data() {
    return {
      question: {
        question_text: '',
        pub_date: ''
      },
      options: [],
      radioOptions: [],
      selectedOption: '',
      isSelected: true,
      showResult: false,
      items: []
    }
  },
  watch: {
    selectedOption: function(value) {
      if (value) {
        this.isSelected = false
      }
    }
  },
  methods: {
    vote() {
      axios
        .get(options + '' + this.selectedOption)
        .then(response => {
          let option = response.data
          return axios.put(options + '' + this.selectedOption + '/', {
            option_text: option.option_text,
            question: option.question,
            vote_count: option.vote_count + 1
          })
        })
        .then(() => {
          return axios
            .get(optionSearch + '' + this.$route.params.questionId)
            .then(response => {
              this.items = response.data.map(option => {
                return {
                  option: option.option_text,
                  vote_count: option.vote_count
                }
              })
            })
        })
        .then(() => {
          this.isSelected = true
          this.showResult = true
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  created() {
    axios
      .get(questions + '' + this.$route.params.questionId)
      .then(response => {
        this.question = {
          question_text: response.data.question_text,
          pub_date: new Date(response.data.pub_date)
        }
      })
      .catch(error => {
        console.log(error)
      })

    axios
      .get(optionSearch + '' + this.$route.params.questionId)
      .then(response => {
        this.options = response.data
        this.radioOptions = this.options.map(option => {
          return {
            text: option.option_text,
            value: option.id
          }
        })
      })
      .catch(error => {
        console.log(error)
      })
  }
}
</script>

<template>
  <b-container>
    <b-card title="New Question : " class="m-5" bg-variant="light">
      <b-alert :show="showError" variant="danger"> Add atleast two options</b-alert>
      <b-form>
        <b-form-group horizontal label="Question :" label-for="question">
          <b-form-input id="question" type="text" placeholder="Ask Something" v-model="question_text" :state="questionState" @input="$v.question_text.$touch()"></b-form-input>
          <b-form-invalid-feedback> Question is necessary</b-form-invalid-feedback>
        </b-form-group>
        <b-form-group horizontal :label="'Option ' + (index + 1) + ' :'" :label-for=" 'option'+ (index + 1) " v-for="(option, index) in options " :key="option.id ">
          <b-form-input :id=" 'option'+ (index + 1) " type="text" placeholder="option " v-model="options[index].option_text " :state="options[index].state" @input="$v.options.$each[index].$touch()"> </b-form-input>
          <b-form-invalid-feedback> Option is necessary</b-form-invalid-feedback>
        </b-form-group>
        <br>
        <b-row>
          <b-col sm="3" class="text-center">
            <b-button variant="info " @click="addOption ">Add Option</b-button>
          </b-col>
          <b-col sm="3" class="text-center">
            <b-button variant="warning " @click="removeOption ">Remove Option</b-button>
          </b-col>
          <b-col sm="3" class="text-center">
            <b-button variant="success " @click="onSubmit">Submit</b-button>
          </b-col>
          <b-col sm="3" class="text-center">
            <b-button variant="danger " @click="onReset">Reset</b-button>
          </b-col>
        </b-row>

      </b-form>
    </b-card>
  </b-container>
</template>
<script>
import { validationMixin } from 'vuelidate'
import { required } from 'vuelidate/lib/validators'
import { questions, options } from '../configurations/developmentApi'
import axios from 'axios'

export default {
  name: 'NewQuestion',
  data() {
    return {
      question_text: '',
      questionState: null,
      options: [
        {
          option_text: '',
          state: null
        },
        {
          option_text: '',
          state: null
        }
      ],
      showError: false
    }
  },
  mixins: [validationMixin],
  validations() {
    return {
      question_text: {
        required
      },
      options: {
        required,
        $each: {
          option_text: {
            required
          }
        }
      }
    }
  },
  methods: {
    onSubmit() {
      this.$v.question_text.$touch()
      if (this.$v.question_text.$error) {
        this.questionState = false
      }
      this.$v.options.$touch()
      if (this.$v.options.$error) {
        this.options.forEach((e, i) => {
          if (this.$v.options.$each[i].$invalid) {
            this.options[i].state = false
          }
        })
      }

      if (this.options.length < 2) {
        this.showError = true
      } else {
        axios
          .post(questions, {
            question_text: this.question_text,
            pub_date: new Date()
          })
          .then(response => {
            let questionId = response.data.id
            this.options.forEach(option => {
              axios
                .post(options, {
                  question: questionId,
                  option_text: option.option_text,
                  vote_count: 0
                })
                .then(response => {
                  // console.log(response)
                })
            })
            this.$router.push('/')
          })
          .catch(error => {
            console.log(error)
          })
      }
    },
    onReset() {
      this.question_text = ''
      this.$v.question_text.$reset()
      this.questionState = null
      this.options = [
        {
          option_text: '',
          state: null
        },
        {
          option_text: '',
          state: null
        }
      ]
      this.options.forEach((e, i) => {
        this.options[i].option_text = ''
      })
      this.$v.options.$reset()
      this.showError = false
    },
    addOption() {
      this.options.push({
        option_text: '',
        state: null
      })
    },
    removeOption() {
      this.options.pop()
    }
  },
  created() {}
}
</script>

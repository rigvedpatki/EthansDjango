import Vue from 'vue'
import Router from 'vue-router'
import IndexPage from '../components/index'
import ErrorPage from '../components/error'
import NewQuestion from '../components/new-question'
import Question from '../components/question'
import Layout from '../components/layout'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Layout',
      component: Layout,
      children: [
        {
          path: '/',
          name: 'IndexPage',
          component: IndexPage
        },
        {
          path: '/question',
          name: 'NewQuestion',
          component: NewQuestion
        },
        {
          path: '/question/:questionId',
          name: 'Question',
          component: Question
        }
      ]
    },
    {
      path: '*',
      name: 'ErrorPage',
      component: ErrorPage
    }
  ]
})

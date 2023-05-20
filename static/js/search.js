const fuseOptions = {
  shouldSort: true,
  includeMatches: true,
  tokenize: true,
  threshold: 0.0,
  location: 0,
  distance: 100,
  maxPatternLength: 32,
  minMatchCharLength: 1,
  keys: [
    { name: "title", weight: 0.8 },
    { name: "contents", weight: 0.5 },
    { name: "tags", weight: 0.3 },
    { name: "categories", weight: 0.3 }
  ]
};

Vue.component("search-result-item", {
  props: ["title", "url", "date", "image", "contents", "tags"],
  template: `
  <div style="display: flex;">
    <div>
      <a :href="url">
        <img alt="" itemprop="image" :src="image" class="image">
      </a>
    </div>
    <div class="description">
      <a :href="url" v-text="title" style="font-weight: bold;"></a>
      <div v-text="contents" class="contents"></div>
      <div class="date" v-text="date"></div>
      <div v-for="tag in tags" class="search-tag" v-text="tag"></div>
    </div>
  </div>`
});

const search = (words, fuse) =>
  _.intersectionBy(...words.map(x => fuse.search(x)), "item.permalink");

const app = new Vue({
  el: "#app",
  mounted: async function() {
    this.fuse = new Fuse((await axios.get("/index.json")).data, fuseOptions);
  },
  data: {
    fuse: {},
    word: "",
    results: []
  },
  watch: {
    word: _.debounce(function(word) {
      this.results = word.length > 0 ? search(word.split(" "), this.fuse) : [];
    }, 500)
  }
});
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

const SearchResultItem = {
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
};

const search = (words, fuse) =>
  _.intersectionBy(...words.map(x => fuse.search(x)), "item.permalink");

const app = Vue.createApp({
  mounted: async function() {
    this.fuse = new Fuse((await axios.get("/Til/index.json")).data, fuseOptions);
  },
  data() {
    return {
      fuse: {},
      word: "",
      results: []
    }
  },
  watch: {
    word: {
      immediate: true,
      handler(val, oldVal) {
        _.debounce(() => {
          this.results = val.length > 0 ? search(val.split(" "), this.fuse) : [];
        }, 500)();
      }
    }
  }
});

app.component('search-result-item', SearchResultItem);
app.mount('#app');

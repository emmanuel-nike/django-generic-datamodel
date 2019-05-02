<template>
  <div
    class="form-group"
    :class="[
       {'has-danger': error},
       {'focused': focused},
       {'has-label': label || $slots.label},
       {'has-success': valid === true},
       {'has-danger': valid === false},
       groupClasses]"
  >
    <slot name="label">
      <label v-if="label" class="form-control-label" :class="labelClasses">
        {{label}}
        <span v-if="required">*</span>
      </label>
    </slot>
    <slot v-bind="slotData">
      <textarea
        v-on="listeners"
        v-bind="$attrs"
        class="form-control"
        :class="[{'is-valid': valid === true}, {'is-invalid': valid === false}, inputClasses]"
        aria-describedby="addon-right addon-left"
      ></textarea>
    </slot>
    <slot name="infoBlock"></slot>
    <slot name="helpBlock">
      <div class="text-danger invalid-feedback" style="display: block;" v-if="error">{{ error }}</div>
    </slot>
  </div>
</template>
<script>
export default {
  inheritAttrs: false,
  name: "base-textarea",
  props: {
    required: {
      type: Boolean,
      description: "Whether input is required (adds an asterix *)"
    },
    valid: {
      type: Boolean,
      description: "Whether is valid",
      default: undefined
    },
    label: {
      type: String,
      description: "Input label (text before input)"
    },
    error: {
      type: String,
      description: "Input error (below input)"
    },
    groupClasses: {
      type: String,
      description: "Div form-group css classes"
    },
    labelClasses: {
      type: String,
      description: "Input label css classes"
    },
    inputClasses: {
      type: String,
      description: "Input css classes"
    },
    value: {
      type: String,
      description: "Input value"
    }
  },
  data() {
    return {
      focused: false
    };
  },
  computed: {
    listeners() {
      return {
        ...this.$listeners,
        input: this.updateValue,
        focus: this.onFocus,
        blur: this.onBlur
      };
    },
    slotData() {
      return {
        focused: this.focused,
        ...this.listeners
      };
    }
  },
  methods: {
    updateValue(evt) {
      let value = evt.target.value;
      this.$emit("input", value);
    },
    onFocus(value) {
      this.focused = true;
      this.$emit("focus", value);
    },
    onBlur(value) {
      this.focused = false;
      this.$emit("blur", value);
    }
  }
};
</script>
<style>
</style>

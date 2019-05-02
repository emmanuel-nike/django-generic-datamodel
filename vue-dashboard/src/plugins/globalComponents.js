import Badge from "../components/Badge";
import BaseAlert from "../components/BaseAlert";
import BaseButton from "../components/BaseButton";
import BaseInput from "../components/BaseInput";
import BaseTextarea from "../components/BaseTextarea";
import BaseSelect from "../components/BaseSelect";
import BaseDropdown from "../components/BaseDropdown";
import BaseNav from "../components/BaseNav";
import BasePagination from "../components/BasePagination";
//import BaseProgress from "../components/BaseProgress";
import BaseTable from "../components/BaseTable";
import BaseHeader from "../components/BaseHeader";
import Card from "../components/Card";
import StatsCard from "../components/StatsCard";
import Modal from "../components/Modal";
//import TabPane from "../components/Tabs/TabPane";
//import Tabs from "../components/Tabs/Tabs";

export default {
  install(Vue) {
    Vue.component(Badge.name, Badge);
    Vue.component(BaseAlert.name, BaseAlert);
    Vue.component(BaseButton.name, BaseButton);
    Vue.component(BaseInput.name, BaseInput);
    Vue.component(BaseTextarea.name, BaseTextarea);
    Vue.component(BaseSelect.name, BaseSelect);
    Vue.component(BaseNav.name, BaseNav);
    Vue.component(BaseDropdown.name, BaseDropdown);
    Vue.component(BasePagination.name, BasePagination);
    //Vue.component(BaseProgress.name, BaseProgress);
    Vue.component(BaseTable.name, BaseTable);
    Vue.component(BaseHeader.name, BaseHeader);
    Vue.component(Card.name, Card);
    Vue.component(StatsCard.name, StatsCard);
    Vue.component(Modal.name, Modal);
    //Vue.component(TabPane.name, TabPane);
    //Vue.component(Tabs.name, Tabs);
  }
};
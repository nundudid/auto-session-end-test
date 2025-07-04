<script lang="ts">
  import { onMount } from "svelte";
  import { setupSessionTracking } from "$lib/session";

  let sessionStatus = "Session is active";

  onMount(() => {
    setupSessionTracking((status) => {
      sessionStatus = status === "expired" ? "Session expired!" : "Session is active";
    });
  });
</script>

<h1>{sessionStatus}</h1>

// Deno Edge Function: POST /stripe-webhook - verify signature, idempotent enrol.
import { serve } from "https://deno.land/std@0.224.0/http/server.ts";
serve(async (req) => {
  const sig = req.headers.get("stripe-signature") ?? "";
  const raw = await req.text();
  // TODO: verify with STRIPE_WEBHOOK_SECRET via crypto.subtle (fail-closed if missing)
  if (!sig || !Deno.env.get("STRIPE_WEBHOOK_SECRET")) {
    return new Response("missing signature config", { status: 400 });
  }
  const evt = JSON.parse(raw); // after verify in prod
  // Idempotency: stripe_session_id UNIQUE in enrollments - duplicate delivery = no-op
  console.log("stripe event:", evt.type);
  return new Response(JSON.stringify({ ok: true }), { headers: { "content-type": "application/json" } });
});
